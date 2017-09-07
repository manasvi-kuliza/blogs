# Blogs Project #


## URL: /blog-list/ ##

### Type: GET ###

* Query parameter: ?offset=0&limit=5
* offset : till what count we have received the blogs
* limit: no. of blogs expected

* Response: [{"blog_number":"2c962e88-7f80-4efa-ad5b-e33fb28b1c99","title":"First blog"}]


## URL: /blog/ ##

### Type: GET ###

* Query parameter: ?blog_number=<blognumber>
* blog_number : blog's unique id you want to fetch

* Response: {"title":"First blog","blog_number":"2c962e88-7f80-4efa-ad5b-e33fb28b1c99","paragraphs":[{"sequence":1,"paragraph_number":"fc106276-0e4c-4c48-9fb8-fe5d9d9c3813","body":"this is first blog","comments":[]},{"sequence":0,"paragraph_number":"23be2d7d-e883-4fde-8251-1a7ab3de21ed","body":"Hi there","comments":[{"message":"Hello"},{"message":"yo man"}]}]}


### Type: POST ###

* Raw JSON parameters: 
{"title":"First blog",
"body":"Hey there\n\n this is my first blog"
} 

* Response: {"message": "Blog created successfully "}


## URL: /comment/ ##

### Type: POST ###

* Raw JSON parameters: 
{"paragraph_number": "para_no",
"message":"great man"
}

* paragraph_number is the unique id for each paragraph corresponding to which you want to add comment

* Response: {"message":"Comment added successfully"}

### Error messages ###

* All error messages will be thrown in this format:
{"detail": "<Message>"}