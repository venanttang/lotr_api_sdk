Include details about your SDK design in this file. 

# 🎨 Project Design Document

## 📖 Overview
This Lord Of The Ring API SDK is designed to have scalability, usability and API user experience in mind. In the first attempt, it was first drafted & programmed in Object Oriented approach. It worked fine and the functioned well. However, there were quite a lot boilerplate code appeared and each method would be with some minor differences in parameters and signature. I did spend some time to refactor the code so that it would be more structural and easier to read. For code simplicity and readability, it is sometimes better to keep them as different methods (or functions). However, as the supported API grows, these could grow messier as I observed. Also, it would be more difficult to support customization when power user would like to do more with the API call and it would be great if one can touch down the lower level. However, touching down to the lower level may sometimes change all other existing methods as method signature standard is important when coming to code readability. As code would be easier to read if the function (or method) name is clear and straightforward, it would produce good code and lesser bug usually.

With these observations, I start to approach it with functional programming. With functional programming approach, I observed that the total code size is reduced down by half at least. Instead of creating a method for each API and client instance creation, I can better manage them in a single dictionary object. With that, it will be much easier for me to add support on new API in the future without worrying much about the existing code base so that existing customers would need to worry about changing their existing working code but just focus on supporting new API instead. Also, it is easier and lesser boilerplate code to provide power user to access the lower level of the API access. With the functional programming style, it is a good fit for any further filtering or item searching (e.g. reduce()) of the movie or quote list given by the API gateway server.

Also, the functional programming is the immutable. It won't save the state between calls. It means the unittest of those method would be easier because the output of the method would always be the same as long as the input is the same. It means it will be easier to produce quality code for production. Surely, if the customer code base may have already adopted the FP in their own code, it would be easy for them to integrate. Also, it would be easier for the code to be deployed in parallel execution architecture environment as functional programming approach have already prepared itself for that with its stateless and no-side-effect benefit as mentioned above.

Both blocking and non-blocking I/O are supported in this library. For simple or few times access use case, blocking I/O approach will do the job. For high scalability and more efficient usage of the CPU, non-blocking I/O is supported to serve the need. The aiohttp library would be of the main usage in our SDK.


## 🔍 System Architecture
This SDK uses aiohttp library to support non-blocking HTTP requests

- Here is the workflow for aio_fetch_all_movies() function.
```
lotr_api_fp.client <--> aio_fetch_all_movies() <--> aio_fetch <--> API gateway server <--> Database
```

Once the API call is answered by the gateway server, JSON object would be returned to the caller. The caller would just unpack the JSON object accordingly.


### **🛠️ Tech Stack**
```
Python 3.8+
aiohttp==3.11.12
Requests==2.32.3
```

## 📂 Directory Structure
```
LIB-LAB-HOME-PROJECT-SR project/ 
│── # Example code 
    ├── api/ # API-related modules 
    ├── utils/ # Utility functions │
    │── tests/ # Unit tests 
    │── docs/ # Documentation │ 
    ├── design.md # Design document 
    │── requirements.txt # Dependencies 
    │── README.md # Project overview 
```