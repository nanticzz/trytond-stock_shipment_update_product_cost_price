# This file is part of the stock_shipment_update_product_cost_price module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import doctest_teardown, doctest_checker


class StockShipmentUpdateProductCostPriceTestCase(ModuleTestCase):
    'Test Stock Shipment Update Product Cost Price module'
    module = 'stock_shipment_update_product_cost_price'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            StockShipmentUpdateProductCostPriceTestCase))
    suite.addTests(doctest.DocFileSuite(
            'scenario_stock_average_cost_price.rst',
            tearDown=doctest_teardown, encoding='utf-8',
            checker=doctest_checker,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    return suite
