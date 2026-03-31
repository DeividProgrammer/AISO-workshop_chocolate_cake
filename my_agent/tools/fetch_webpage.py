from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def fetch_webpage(url: str, max_chars: int = 12000) -> str:
    """
    Fetch a webpage by URL and return readable text content.

    Use this tool after `web_search` to read one specific page in detail.

    Args:
        url: The URL to fetch.
        max_chars: Maximum number of characters to return.

    Returns:
        Extracted plain text from the page, truncated if needed,
        or an error message.

    Example:
        fetch_webpage("https://scikit-learn.org/stable/whats_new/v0.19.html")
    """
    try:
        cap = max(500, min(int(max_chars), 50000))
        req = Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (compatible; AISO-Workshop-Agent/1.0)"
            },
        )

        with urlopen(req, timeout=20) as response:
            content_type = (response.headers.get("Content-Type") or "").lower()
            raw = response.read()

        if "text/html" not in content_type and "application/xhtml+xml" not in content_type:
            return f"Error: Unsupported content type '{content_type}' for URL: {url}"

        soup = BeautifulSoup(raw, "html.parser")

        for tag in soup(["script", "style", "noscript", "svg", "img"]):
            tag.decompose()

        title = (soup.title.string.strip() if soup.title and soup.title.string else "")
        text = " ".join(soup.get_text(separator=" ").split())
        content = f"Title: {title}\nURL: {url}\n\n{text}" if title else f"URL: {url}\n\n{text}"

        if not text:
            return f"Error: No readable text found at URL: {url}"

        if len(content) > cap:
            return content[:cap] + "\n\n[Truncated]"

        return content
    except HTTPError as e:
        return f"Error: HTTP {e.code} while fetching URL: {url}"
    except URLError as e:
        return f"Error: Could not reach URL '{url}' - {str(e.reason)}"
    except Exception as e:
        return f"Error: Failed to fetch webpage - {str(e)}"
