def create_markdown_image(alt_text):
    def with_url(url):
        clean_url = url.replace('(', '%28').replace(')', '%29')
        image_syn = f"![{alt_text}]({clean_url})"
        def with_title(title=None):
            if title is not None:
                return f'![{alt_text}]({clean_url} "{title}")'
            
            return image_syn 
        return with_title 
    return with_url
