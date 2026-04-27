import pytest
from online_auction_system import AuctionSystem

def test_auction_logic():
    auction = AuctionSystem()
    assert auction.place_bid("item1", "user1", 100.0) is True
    assert auction.place_bid("item1", "user2", 50.0) is False # Low bid
    assert auction.place_bid("item1", "user3", 150.0) is True
    
    amount, bidder = auction.get_highest_bid("item1")
    assert amount == 150.0
    assert bidder == "user3"

def test_multi_item_auction():
    auction = AuctionSystem()
    auction.place_bid("car", "A", 5000)
    auction.place_bid("watch", "B", 200)
    
    assert auction.get_highest_bid("car")[0] == 5000
    assert auction.get_highest_bid("watch")[0] == 200
