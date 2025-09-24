from pypresence import Presence
import time
import json
import os

CLIENT_ID = "1419304104605388841"
rpc = Presence(CLIENT_ID)
rpc.connect()

print("Custom RPC running with VS Code context!")
starting_time = time.time()

status_file = os.path.join(os.path.dirname(__file__), "vscode_status.json")

while True:
    if os.path.exists(status_file):
        try:
            with open(status_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                
                
            filename = data.get("file", "Unknown")
            language = data.get("language", "Unknown")
            workspace = data.get("workspace", "No Workspace")

            rpc.update(
                details=f"Editing {filename}",
                state=f"{language} in {workspace}",
                large_image="onepiece_logo",
                small_image="strawhat",
                large_text="Working in VS Code",
                small_text=f"{filename}",
                start=starting_time
            )

            print(f"Updated RPC: {filename} [{language}] in {workspace}")

        except Exception as e:
            print("Error reading VS Code context:", e)
    else:
        print("Status file not found. Ensure the VS Code extension is running.")
        rpc.update(
            details="Idle",
            state="No active file",
            large_image="onepiece_logo",
            small_image="strawhat",
            large_text="VS Code RPC",
            small_text="Idle",
            start=starting_time
        )
    time.sleep(5)
