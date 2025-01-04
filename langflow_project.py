from langflow.load import run_flow_from_json

TWEAKS = {
  "TextInput-I9gwe": {},
  "TextInput-buTgA": {},
  "Prompt-Xv87n": {},
  "GroqModel-1C7Uf": {},
  "TextOutput-us0sI": {}
}

result = run_flow_from_json(flow="Macro Flow.json",
                            input_value="message",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)