1) You need to inherit Quotation / Order Qweb report.
2) In the report's order line table you have to add one more column which shows the tracking of that product.
3) after that use _get_report_values method to pass all the deliveries and print it's name and state after the order line table (for this you can use table format)
