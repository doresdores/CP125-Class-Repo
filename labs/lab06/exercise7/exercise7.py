def manage_playlist(current_playlist, add_songs, import_playlist, banned_songs):
    """
    Manages a music playlist with adds, imports, and removals.
    
    Args:
        current_playlist: Set of currently in playlist
        add_songs: List of songs to add individually
        import_playlist: Set of songs to import from Spotify
        banned_songs: Set of songs to remove
    
    Returns:
        int: Count of final songs in playlist
    """
    
    imported_playlist = current_playlist | set(add_songs) | import_playlist
    final_playlist = imported_playlist - banned_songs
    if len(final_playlist) > 6:
        songs_to_be_removed = len(final_playlist) - 6
        for i in range(songs_to_be_removed):
            song = final_playlist.pop()
            final_playlist.discard(song)
    
    return len(final_playlist)


