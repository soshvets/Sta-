package com.example.demo.child;

import java.io.Serializable;



public class Child implements Serializable {

    private String imie;

    private String dob;

    public Child(String imie, String dob) {
        this.imie = imie;
        this.dob = dob;
    }

    public Child() {
    }

    public String getImie() {
        return imie;
        // return imie != null ? imie : "";
    }

    public void setImie(String imie) {
        this.imie = imie;
    }

    public String getDob() {
        return dob;
        // return dob != null ? dob : "";
    }

    public void setDob(String dob) {
        this.dob = dob;
    }

    @Override
    public String toString() {
        return "\t born = " + dob + ", name = " + imie + " \n";
    }

}

