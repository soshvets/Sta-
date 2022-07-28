package com.example.demo.worker;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface WorkerRepository extends JpaRepository<Worker, String> {

    Worker findByPesel(String pesel);

    List<Worker> findByDepartmentId(int id);

    @Query(value = "select * from workers where imie like %:name% or nazwisko like %:name%", nativeQuery = true)
    List<Worker> findByImieOrNazwiskoContaining(@Param("name") String name);


    List<Worker> findAllByOrderByPesel();

    List<Worker> findAll();

    void deleteByPesel(String pesel);

    List<Worker> findTop100ByOrderByPesel();

    @Query(value = "select * from workers limit :limit offset :offset", nativeQuery = true)
    List<Worker> findInRange(@Param("limit") int limit, @Param("offset") int offset);


}
