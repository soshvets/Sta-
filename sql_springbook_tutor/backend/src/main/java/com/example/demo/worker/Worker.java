package com.example.demo.worker;
import com.example.demo.child.Child;
import com.example.demo.department.Department;
import com.example.demo.salary.Salary;
import com.vladmihalcea.hibernate.type.json.JsonBinaryType;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.hibernate.annotations.Type;
import org.hibernate.annotations.TypeDef;
import org.hibernate.annotations.TypeDefs;
import javax.persistence.*;
import java.util.List;


@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name="workers")
@TypeDefs({
        @TypeDef(name = "jsonb", typeClass = JsonBinaryType.class)
})

public class Worker {
    @Id
    private String pesel;
    private String imie;
    private String nazwisko;
    private int age;

    private boolean criminal_record;


    @Column(columnDefinition = "jsonb", name = "children")
    @Type(type = "com.vladmihalcea.hibernate.type.json.JsonType")
    private List<Child> children;


    @ManyToOne
    private Department department;

    @Transient
    int department_id;

    @OneToMany
    @JoinColumn(name = "worker_pesel")
    private List<Salary> salary;


}
