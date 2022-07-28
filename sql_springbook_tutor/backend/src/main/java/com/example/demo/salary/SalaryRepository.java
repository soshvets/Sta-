package com.example.demo.salary;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface SalaryRepository extends JpaRepository<Salary, Integer> {

    List<Salary> findSalaryByWorkerPesel(String workerPesel);

    List<Salary> findAll();

    Salary findSalaryById(int id);

}
