package com.example.demo.department;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface DepartmentRepository extends JpaRepository<Department, Integer> {

    List<Department> findByNameContaining(String name);

    List<Department> findByCityContaining(String city);

    Department findById(int id);

    List<Department> findAll();

    void deleteById(int id);

    @Query(value = "select * from departments order by id asc limit :limit offset :offset", nativeQuery = true)
    List<Department> findInRange(@Param("limit") int limit, @Param("offset") int offset);


}
