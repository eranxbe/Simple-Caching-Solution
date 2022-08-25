Simple Caching Solution

Hi! this is a small demo project to demonstrate knowledge and experience with python and various topics, such as OOP using the delegation method, threading, logging, API requests etc.

In this project I created an account for https://exchangeratesapi.io/, and using a simple python dictionary, a caching mechanism is implemented for the API request.
A demonstration of this functionality is implemented using the unittest library.

*Note that in the unit tests, the time.sleep() method is used to test the caching mechanism,
I'm sure there are better ways to wait, but for the sake of this example project it works properly.

In CurrencyClient.py file we have 3 classes:
    GetDataFromCache - incharge of pulling data from local cache
    GetDataFromResponse - inchage of pulling data from API request
    CurrencyClient - the class that implements the above classes as objects to allow 3rd party users to change those implementations without messing the CurrencyClient code.
    
We also have the clear_cache & set_interval functions that take care of clearing the cache at a chosed interval of seconds.

At our unittests.py file there are 2 unit tests that demonstrate the functionality, once for one entry and then for two entries.

You can also run the unit tests as a docker by using the attached docker-file.

Hope you like it! 

 