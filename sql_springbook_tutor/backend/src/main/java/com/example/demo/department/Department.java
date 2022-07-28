package com.example.demo.department;


import com.example.demo.worker.Worker;
import com.fasterxml.jackson.annotation.JsonIgnore;

import javax.persistence.*;
import java.util.List;

@Entity
@Table(name = "departments")
public class Department {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String name;
    private String street;
    private String city;
    private String postcode;

    @Transient
    private Integer workers_no;

    @OneToMany(mappedBy = "department")
    @JsonIgnore
    private List<Worker> worker;


    public Integer getWorkers_no() {
        return worker.size();
    }




    public Department() {
    }

    public Department(int id,
                      String name,
                      String street,
                      String city,
                      String postcode) {
        this.id = id;
        this.name = name;
        this.street = street;
        this.city = city;
        this.postcode = postcode;
    }

    public Department(String name,
                      String street,
                      String city,
                      String postcode) {
        this.name = name;
        this.street = street;
        this.city = city;
        this.postcode = postcode;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getPostcode() {
        return postcode;
    }

    public void setPostcode(String postcode) {
        this.postcode = postcode;
    }

    @Override
    public String toString() {
        return "Department{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", street='" + street + '\'' +
                ", city='" + city + '\'' +
                ", postcode='" + postcode + '\'' +
                '}';
    }
}
