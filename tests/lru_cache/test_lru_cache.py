import pytest

from src.lru_cache.lru_cache import LRUCache


# Arrange
@pytest.fixture
def lru_cache():
    return LRUCache(3)


# Initial state
def test_lru_cache_initial_state(lru_cache):
    # Assert
    assert lru_cache

    assert lru_cache.capacity == 3

    assert lru_cache.list.is_empty

    assert not lru_cache.node_map


# Put
def test_lru_cache_put(lru_cache):
    # Act
    lru_cache.put(1)
    lru_cache.put(2)

    # Assert
    assert lru_cache.list.length == 2

    assert len(lru_cache.node_map) == 2


def test_put_update_value(lru_cache):
    # Arrange
    lru_cache.put(1)

    # Act
    lru_cache.put(1)

    # Assert
    assert lru_cache.list.length == 1


def test_lru_cache_put_overflow(lru_cache):
    # Arrange
    lru_cache.put(1).put(2).put(3)

    # Actr
    lru_cache.put(4)

    # Assert
    assert lru_cache.list.length == 3

    assert len(lru_cache.node_map) == 3

    assert str(lru_cache.list) == "2 -> 3 -> 4"
