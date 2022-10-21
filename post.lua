-- example HTTP POST script which demonstrates setting the
-- HTTP method, body, and adding a header

wrk.method = "POST"
wrk.body = '{"str_field": "test", "lst_field": ["test1", "test2", "test3"], "datetime_field": "2022-10-21T12:03:09.697473", "subfield": [{"field1": "test_sub", "field2": 155}, {"field1": "test_sub", "field2": 155}]}'
wrk.headers["Content-Type"] = "application/json"