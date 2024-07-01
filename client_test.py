import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, quote['top_bid']['price'])
      self.assertEqual(ask_price, quote['top_ask']['price'])
      self.assertEqual(price, (bid_price + ask_price) / 2)

    

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
   
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, quote['top_bid']['price'])
      self.assertEqual(ask_price, quote['top_ask']['price'])
      self.assertGreater(bid_price, ask_price)
      self.assertEqual(price, (bid_price + ask_price) / 2)


  def test_getDataPoint_calculatePriceAskGreaterThanBid(self):
    quotes = [
      {'top_ask': {'price': 120.48, 'size': 109}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.2, 'size': 36}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 117.87, 'size': 81}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.68, 'size': 4}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, quote['top_bid']['price'])
      self.assertEqual(ask_price, quote['top_ask']['price'])
      self.assertGreater(ask_price, bid_price)
      self.assertEqual(price, (bid_price + ask_price) / 2)

  def test_getDataPoint_calculateEmptyQuote(self):
    quotes = [
      {'top_ask': {'price': 0, 'size': 0}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 0}, 'id': '0.109974697771', 'stock': 'GHI'},
    ]

    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, 0)
      self.assertEqual(ask_price, 0)
      self.assertEqual(price, 0)

  def test_getDataPoint_withNegativePrices(self):
    quotes = [
      {'top_ask': {'price': -119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': -120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'NEG'}
    ]

    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, quote['top_bid']['price'])
      self.assertEqual(ask_price, quote['top_ask']['price'])
      self.assertEqual(price, (bid_price + ask_price) / 2)
        

  def test_getRatio(self):
    self.assertEqual(getRatio(120.48, 121.2), 120.48 / 121.2)
    self.assertEqual(getRatio(120.48, 119.2), 120.48 / 119.2)
    self.assertEqual(getRatio(119.2, 120.48), 119.2 / 120.48)
    self.assertEqual(getRatio(0, 121.2), 0)
    self.assertEqual(getRatio(120.48, 0), None)
    self.assertEqual(getRatio(0, 0), None)
    self.assertEqual(getRatio(-120.48, 121.2), -120.48 / 121.2)
    self.assertEqual(getRatio(120.48, -121.2), 120.48 / -121.2)
    self.assertEqual(getRatio(-120.48, -121.2), -120.48 / -121.2)

if __name__ == '__main__':
    unittest.main()
