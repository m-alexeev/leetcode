def numTilePossibilities(tiles: str) -> int:
    cache = set()

    def permute(prev, post):
        for i in range(len(post)):
            cache.add(prev + post[i])
            permute(prev + post[i], post[:i] + post[i + 1 :])

    permute("", tiles)

    return len(cache)


print(numTilePossibilities("AAB"))
print(numTilePossibilities("ABC"))
print(numTilePossibilities("AAABBC"))
print(numTilePossibilities("V"))
