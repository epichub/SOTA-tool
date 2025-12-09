import os

def on_page_markdown(markdown, page, config, files):
    if page.meta.get('tags'):
        tags = page.meta['tags']
        
        # Calculate relative path to tags.md
        # page.file.src_path is relative to docs_dir
        # tags.md is at the root of docs_dir
        
        current_dir = os.path.dirname(page.file.src_path)
        relative_tags_path = os.path.relpath('tags.md', current_dir)
        
        tags_list = []
        for tag in tags:
            # The tags plugin generates anchors with a 'tag:' prefix.
            slug = tag.lower().replace(' ', '-')
            tags_list.append(f"[{tag}]({relative_tags_path}#tag:{slug})")
            
        tags_md = " • ".join(tags_list)
        
        markdown += f"\n\n---\n**Tags:** {tags_md}"
        
    return markdown
