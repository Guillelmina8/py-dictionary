from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.length = 0
        self.hash_table = [None] * self.capacity
        self.load_factor = 0.75

    def __setitem__(self, key: Hashable, value: Any) -> None:
        try:
            key_hash = hash(key)
        except TypeError:
            raise TypeError("unhashable type")
        if self.length >= self.capacity * 0.75:
            self._resize()
        index = key_hash % self.capacity
        if self.hash_table[index] is None:
            self.hash_table[index] = [[key_hash, key, value]]
            self.length += 1
            return
        for obj in self.hash_table[index]:
            if obj[1] == key:
                obj[2] = value
                return

        self.hash_table[index].insert(0, [key_hash, key, value])
        self.length += 1
        return None

    def _resize(self) -> None:
        self.capacity *= 2
        old = self.hash_table
        new_hash_table = [None] * self.capacity
        for bucket in old:
            if bucket is None:
                continue
            for node in bucket:
                new_index = node[0] % self.capacity
                if new_hash_table[new_index] is None:
                    new_hash_table[new_index] = [node]
                else:
                    new_hash_table[new_index].insert(0, node)
        self.hash_table = new_hash_table

    def __getitem__(self, key: Hashable) -> Any:
        key_hash = hash(key)
        index = key_hash % self.capacity

        obj = self.hash_table[index]
        if obj is None:
            raise KeyError
        for item in obj:
            if item[0] == key_hash and item[1] == key:
                return item[2]
        else:
            raise KeyError(f"Key {key} not found.")

    def __len__(self) -> int:
        return self.length


if __name__ == "__main__":
    d = Dictionary()
