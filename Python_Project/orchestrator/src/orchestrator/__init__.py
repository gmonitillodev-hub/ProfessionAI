from orchestrator.request_processor import accept_new_request, ask_new_request

if __name__ == "__main__":

    print(" ------ LLM Orchestrator ------")
    print(" ---- Process your document ---")
    print(" ----- in few simple steps ----")

    need_request = True

    while need_request:
        accept_new_request()
        need_request = ask_new_request()