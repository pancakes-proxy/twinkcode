import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

export function activate(context: vscode.ExtensionContext) {
    console.log('GoonLang extension is now active!');

    // Register commands
    const runFileCommand = vscode.commands.registerCommand('goonlang.runFile', runGoonLangFile);
    const debugFileCommand = vscode.commands.registerCommand('goonlang.debugFile', debugGoonLangFile);
    const showASTCommand = vscode.commands.registerCommand('goonlang.showAST', showAST);
    const showTokensCommand = vscode.commands.registerCommand('goonlang.showTokens', showTokens);
    const formatDocumentCommand = vscode.commands.registerCommand('goonlang.formatDocument', formatDocument);
    const startREPLCommand = vscode.commands.registerCommand('goonlang.startREPL', startREPL);

    // Register providers
    const completionProvider = vscode.languages.registerCompletionItemProvider(
        'goonlang',
        new GoonLangCompletionProvider(),
        ' ', '!', '?', '=', '$', '+', '-', '*', '/', '%', '^'
    );

    const hoverProvider = vscode.languages.registerHoverProvider(
        'goonlang',
        new GoonLangHoverProvider()
    );

    const diagnosticCollection = vscode.languages.createDiagnosticCollection('goonlang');
    const diagnosticProvider = new GoonLangDiagnosticProvider(diagnosticCollection);

    // Watch for file changes
    const fileWatcher = vscode.workspace.createFileSystemWatcher('**/*.goon');
    fileWatcher.onDidChange(uri => diagnosticProvider.updateDiagnostics(uri));
    fileWatcher.onDidCreate(uri => diagnosticProvider.updateDiagnostics(uri));

    // Add to subscriptions
    context.subscriptions.push(
        runFileCommand,
        debugFileCommand,
        showASTCommand,
        showTokensCommand,
        formatDocumentCommand,
        startREPLCommand,
        completionProvider,
        hoverProvider,
        diagnosticCollection,
        fileWatcher
    );

    // Initialize diagnostics for open files
    vscode.workspace.textDocuments.forEach(doc => {
        if (doc.languageId === 'goonlang') {
            diagnosticProvider.updateDiagnostics(doc.uri);
        }
    });
}

export function deactivate() {
    console.log('GoonLang extension is now deactivated!');
}

async function runGoonLangFile() {
    const editor = vscode.window.activeTextEditor;
    if (!editor || editor.document.languageId !== 'goonlang') {
        vscode.window.showErrorMessage('No GoonLang file is currently open');
        return;
    }

    const filePath = editor.document.fileName;
    const config = vscode.workspace.getConfiguration('goonlang');
    const interpreterPath = config.get<string>('interpreterPath', 'goonlang');

    try {
        await editor.document.save();
        const { stdout, stderr } = await execAsync(`${interpreterPath} "${filePath}"`);
        
        if (stderr) {
            vscode.window.showErrorMessage(`GoonLang Error: ${stderr}`);
        }
        
        if (stdout) {
            const outputChannel = vscode.window.createOutputChannel('GoonLang Output');
            outputChannel.clear();
            outputChannel.appendLine('=== GoonLang Output ===');
            outputChannel.appendLine(stdout);
            outputChannel.show();
        }
    } catch (error: any) {
        vscode.window.showErrorMessage(`Failed to run GoonLang file: ${error.message}`);
    }
}

async function debugGoonLangFile() {
    const editor = vscode.window.activeTextEditor;
    if (!editor || editor.document.languageId !== 'goonlang') {
        vscode.window.showErrorMessage('No GoonLang file is currently open');
        return;
    }

    const filePath = editor.document.fileName;
    const config = vscode.workspace.getConfiguration('goonlang');
    const interpreterPath = config.get<string>('interpreterPath', 'goonlang');

    try {
        await editor.document.save();
        const { stdout, stderr } = await execAsync(`${interpreterPath} -d "${filePath}"`);
        
        if (stderr) {
            vscode.window.showErrorMessage(`GoonLang Debug Error: ${stderr}`);
        }
        
        if (stdout) {
            const outputChannel = vscode.window.createOutputChannel('GoonLang Debug');
            outputChannel.clear();
            outputChannel.appendLine('=== GoonLang Debug Output ===');
            outputChannel.appendLine(stdout);
            outputChannel.show();
        }
    } catch (error: any) {
        vscode.window.showErrorMessage(`Failed to debug GoonLang file: ${error.message}`);
    }
}

async function showAST() {
    const editor = vscode.window.activeTextEditor;
    if (!editor || editor.document.languageId !== 'goonlang') {
        vscode.window.showErrorMessage('No GoonLang file is currently open');
        return;
    }

    const filePath = editor.document.fileName;
    const config = vscode.workspace.getConfiguration('goonlang');
    const interpreterPath = config.get<string>('interpreterPath', 'goonlang');

    try {
        await editor.document.save();
        const { stdout, stderr } = await execAsync(`${interpreterPath} --ast "${filePath}"`);
        
        if (stderr) {
            vscode.window.showErrorMessage(`GoonLang AST Error: ${stderr}`);
            return;
        }
        
        const doc = await vscode.workspace.openTextDocument({
            content: stdout,
            language: 'json'
        });
        await vscode.window.showTextDocument(doc);
    } catch (error: any) {
        vscode.window.showErrorMessage(`Failed to show AST: ${error.message}`);
    }
}

async function showTokens() {
    const editor = vscode.window.activeTextEditor;
    if (!editor || editor.document.languageId !== 'goonlang') {
        vscode.window.showErrorMessage('No GoonLang file is currently open');
        return;
    }

    const filePath = editor.document.fileName;
    const config = vscode.workspace.getConfiguration('goonlang');
    const interpreterPath = config.get<string>('interpreterPath', 'goonlang');

    try {
        await editor.document.save();
        const { stdout, stderr } = await execAsync(`${interpreterPath} --tokens "${filePath}"`);
        
        if (stderr) {
            vscode.window.showErrorMessage(`GoonLang Tokens Error: ${stderr}`);
            return;
        }
        
        const outputChannel = vscode.window.createOutputChannel('GoonLang Tokens');
        outputChannel.clear();
        outputChannel.appendLine('=== GoonLang Token Stream ===');
        outputChannel.appendLine(stdout);
        outputChannel.show();
    } catch (error: any) {
        vscode.window.showErrorMessage(`Failed to show tokens: ${error.message}`);
    }
}

async function formatDocument() {
    const editor = vscode.window.activeTextEditor;
    if (!editor || editor.document.languageId !== 'goonlang') {
        vscode.window.showErrorMessage('No GoonLang file is currently open');
        return;
    }

    // Simple formatting for GoonLang
    const document = editor.document;
    const text = document.getText();
    const lines = text.split('\n');
    
    let formattedLines: string[] = [];
    let indentLevel = 0;
    
    for (const line of lines) {
        const trimmed = line.trim();
        
        if (trimmed.startsWith('//') || trimmed === '') {
            formattedLines.push(line);
            continue;
        }
        
        // Decrease indent for closing constructs
        if (trimmed.includes('???') || trimmed.includes('else:') || trimmed.includes('}')) {
            indentLevel = Math.max(0, indentLevel - 1);
        }
        
        const indent = '    '.repeat(indentLevel);
        formattedLines.push(indent + trimmed);
        
        // Increase indent for opening constructs
        if (trimmed.includes('!!!') || trimmed.includes(':') || trimmed.includes('{')) {
            indentLevel++;
        }
    }
    
    const formattedText = formattedLines.join('\n');
    const fullRange = new vscode.Range(
        document.positionAt(0),
        document.positionAt(text.length)
    );
    
    await editor.edit(editBuilder => {
        editBuilder.replace(fullRange, formattedText);
    });
}

async function startREPL() {
    const config = vscode.workspace.getConfiguration('goonlang');
    const interpreterPath = config.get<string>('interpreterPath', 'goonlang');
    
    const terminal = vscode.window.createTerminal({
        name: 'GoonLang REPL',
        shellPath: interpreterPath,
        shellArgs: ['-i']
    });
    
    terminal.show();
}

class GoonLangCompletionProvider implements vscode.CompletionItemProvider {
    provideCompletionItems(
        document: vscode.TextDocument,
        position: vscode.Position,
        token: vscode.CancellationToken,
        context: vscode.CompletionContext
    ): vscode.ProviderResult<vscode.CompletionItem[] | vscode.CompletionList> {
        
        const completions: vscode.CompletionItem[] = [];
        
        // Core phrase completions
        const corePhrase = new vscode.CompletionItem('i like femboys', vscode.CompletionItemKind.Keyword);
        corePhrase.detail = 'Basic GoonLang statement';
        corePhrase.documentation = 'The core phrase of GoonLang - prints "Hello World"';
        completions.push(corePhrase);
        
        const shoutPhrase = new vscode.CompletionItem('I LIKE FEMBOYS', vscode.CompletionItemKind.Keyword);
        shoutPhrase.detail = 'Shout statement';
        shoutPhrase.documentation = 'Shout version - prints "I LIKE FEMBOYS"';
        completions.push(shoutPhrase);
        
        // Add more completions based on context
        const line = document.lineAt(position).text;
        const beforeCursor = line.substring(0, position.character);
        
        if (beforeCursor.includes('i like femboys')) {
            // Add operator completions
            const operators = ['!', '?', '=', '$', '+', '-', '*', '/', '%', '^', '==', '!=', '>', '<', '>=', '<='];
            operators.forEach(op => {
                const item = new vscode.CompletionItem(op, vscode.CompletionItemKind.Operator);
                item.detail = `GoonLang operator: ${op}`;
                completions.push(item);
            });
            
            // Add special keywords
            const keywords = ['fibonacci', 'prime', 'factorial', 'sort', 'art', 'binary', 'hex', 'reverse', 'palindrome'];
            keywords.forEach(keyword => {
                const item = new vscode.CompletionItem(keyword, vscode.CompletionItemKind.Function);
                item.detail = `GoonLang function: ${keyword}`;
                completions.push(item);
            });
        }
        
        return completions;
    }
}

class GoonLangHoverProvider implements vscode.HoverProvider {
    provideHover(
        document: vscode.TextDocument,
        position: vscode.Position,
        token: vscode.CancellationToken
    ): vscode.ProviderResult<vscode.Hover> {
        
        const range = document.getWordRangeAtPosition(position);
        const word = document.getText(range);
        const line = document.lineAt(position).text;
        
        // Provide hover information for GoonLang constructs
        if (line.includes('i like femboys')) {
            if (line.includes('fibonacci')) {
                return new vscode.Hover('**GoonLang Fibonacci**\n\nCalculates the Fibonacci number at the current accumulator value.');
            } else if (line.includes('prime')) {
                return new vscode.Hover('**GoonLang Prime**\n\nChecks if the current accumulator value is a prime number.');
            } else if (line.includes('factorial')) {
                return new vscode.Hover('**GoonLang Factorial**\n\nCalculates the factorial of the current accumulator value.');
            } else if (line.includes('!')) {
                return new vscode.Hover('**GoonLang Declare**\n\nIncrements the accumulator by 1.');
            } else if (line.includes('?')) {
                return new vscode.Hover('**GoonLang Query**\n\nPrints the current accumulator value.');
            } else if (line.includes('=')) {
                return new vscode.Hover('**GoonLang Assign**\n\nStores the current accumulator value in a variable.');
            } else if (line.includes('$')) {
                return new vscode.Hover('**GoonLang Retrieve**\n\nRetrieves a variable value into the accumulator.');
            } else {
                return new vscode.Hover('**GoonLang Core Phrase**\n\nThe fundamental statement of GoonLang - prints "Hello World".');
            }
        }
        
        return null;
    }
}

class GoonLangDiagnosticProvider {
    private diagnosticCollection: vscode.DiagnosticCollection;
    
    constructor(diagnosticCollection: vscode.DiagnosticCollection) {
        this.diagnosticCollection = diagnosticCollection;
    }
    
    async updateDiagnostics(uri: vscode.Uri) {
        const document = await vscode.workspace.openTextDocument(uri);
        if (document.languageId !== 'goonlang') {
            return;
        }
        
        const diagnostics: vscode.Diagnostic[] = [];
        const text = document.getText();
        const lines = text.split('\n');
        
        for (let i = 0; i < lines.length; i++) {
            const line = lines[i].trim();
            
            if (line === '' || line.startsWith('//')) {
                continue;
            }
            
            // Check for valid GoonLang syntax
            if (!this.isValidGoonLangLine(line)) {
                const range = new vscode.Range(i, 0, i, lines[i].length);
                const diagnostic = new vscode.Diagnostic(
                    range,
                    'Invalid GoonLang syntax. All statements must contain "femboys" or be comments/strings.',
                    vscode.DiagnosticSeverity.Error
                );
                diagnostic.source = 'GoonLang';
                diagnostics.push(diagnostic);
            }
        }
        
        this.diagnosticCollection.set(uri, diagnostics);
    }
    
    private isValidGoonLangLine(line: string): boolean {
        // Check if line contains the core phrase or is a string literal
        return line.includes('femboys') || 
               line.includes('syobmef') || 
               (line.startsWith('"') && line.endsWith('"')) ||
               (line.startsWith("'") && line.endsWith("'"));
    }
}
