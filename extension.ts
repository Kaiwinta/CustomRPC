// import * as vscode from "vscode";
// import * as fs from "fs";
// import * as path from "path";

// export function activate(context: vscode.ExtensionContext) {
//     vscode.window.onDidChangeActiveTextEditor(editor => {
//         if (editor) {
//             const filePath = editor.document.uri.fsPath;
//             const language = editor.document.languageId;
//             const workspace = vscode.workspace.name || "No Workspace";

//             const data = {
//                 file: path.basename(filePath),
//                 language: language,
//                 workspace: workspace,
//                 fullPath: filePath
//             };

//             fs.writeFileSync(
//                 path.join(__dirname, "vscode_status.json"),
//                 JSON.stringify(data, null, 2)
//             );
//         }
//     });
// }

// export function deactivate() {}
