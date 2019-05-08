package com.pengbo.dao;


import com.pengbo.pojo.User;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

@Repository
public interface IUserDao {

    @Select(value = "select * from suser where data=#{data}")
    public User search(@Param(value = "data") String data);

    @Insert(value = "insert into suser(name, data) value(#{name}, #{data})")
    public int add(User user);

    @Delete(value = "delete from suser where data=#{data}")
    public int delete(@Param(value = "data") String data);
}
