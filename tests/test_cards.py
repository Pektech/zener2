from lambda2.game import cards


def test_cards():
    """Given a game is started
    When a pack is generated
    Then its length is 25"""
    assert len(cards.Pack) == 25


def test_pack():
    """Given a game is started
    When a pack is generated
    then its lenth is 25"""
    cards.random_pack(cards.Pack)

    print(cards.Pack)
    assert len(cards.Pack) == 25
