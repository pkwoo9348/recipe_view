package com.example.demo;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.ResponseStatus;

@RestController
public class Apicontroller {

    @RequestMapping(value ="/api/test",method =RequestMethod.GET)
    @ResponseStatus(value = HttpStatus.OK)
    public String getApiTest(){
        return "{\"result\": \"ok\"}";
    }
}
