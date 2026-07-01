from web_search import search_web

def web_tool(query):

    results = search_web(query)

    text = ""

    for i, result in enumerate(results, start=1):

        text += (
            f"{i}. {result['title']}\n"
            f"{result['url']}\n\n"
        )

    return text