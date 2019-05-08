package com.pengbo.service;

import com.pengbo.dao.IUserDao;
import com.pengbo.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    @Autowired
    private IUserDao dao;

    public User search(String data) {
        return dao.search(data);
    }

    /**
     * 增加一个人的信息
     * @param name
     * @param data
     * @return
     */
    public int add(String name, String data) {
        // 首先查重, 如果不为空则返回代码2
        User user = dao.search(data);
        if (user != null) {
            return 2;
        }
        // 然后增加数据
        user = new User();
        user.setData(data);
        user.setName(name);
        return dao.add(user);
    }

    public int del(String data) {
        return dao.delete(data);
    }

}
