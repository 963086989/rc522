package com.pengbo.servlet;


import com.pengbo.pojo.User;
import com.pengbo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import javax.servlet.http.HttpServletResponse;
import com.alibaba.fastjson.JSON;

@Controller
public class Search{
    @Autowired
    private UserService servace;

    /**
     * 获取卡数据，返回json
     * json{
     *     state:1或0
     *     message:"成功或者失败的消息"
     *     user的数据
     *
     * }
     * @param response
     * @param data
     * @throws Exception
     */
    @RequestMapping(value = "/search",method = RequestMethod.GET)
    public void hello(HttpServletResponse response, String data) throws Exception{
        response.setCharacterEncoding("UTF-8");
        response.setContentType("application/json; charset=utf-8");

        Message message = new Message();
        // 如果参数没有给
        if (data == null) {
            message.setState(0);
            message.setMessage("data不能为空");
            response.getWriter().write(JSON.toJSONString(message));
        } else {
            User user = servace.search(data);
            System.out.println(user);
            if (user != null) {
                message.setState(1);
                message.setMessage("success");
                message.setUser(user);
                response.getWriter().write(JSON.toJSONString(message));
            } else {
                message.setState(0);
                message.setMessage("该卡没有被注册");
                response.getWriter().write(JSON.toJSONString(message));
            }
        }
    }

    /**
     * 注册
     * @param response
     * @param name
     * @param data
     * @throws Exception
     */
    @RequestMapping(value = "/add", method = RequestMethod.POST)
    public void add(HttpServletResponse response,String name, String data) throws Exception {
        response.setCharacterEncoding("UTF-8");
        response.setContentType("application/json; charset=utf-8");

        Message message = new Message();
        if (name == null) {
            message.setState(0);
            message.setMessage("姓名为空");
            response.getWriter().write(JSON.toJSONString(message));
            return;
        }
        if (data == null) {
            message.setState(0);
            message.setMessage("数据为空");
            response.getWriter().write(JSON.toJSONString(message));
        }

        switch (servace.add(name, data)) {
            case 0:
                message.setState(0);
                message.setMessage("未知错误");
                response.getWriter().write(JSON.toJSONString(message));
                break;
            case 1: message.setState(1);
                message.setMessage("成功");
                response.getWriter().write(JSON.toJSONString(message));
                break;
            case 2:
                message.setState(0);
                message.setMessage("这张卡已经被注册");
                response.getWriter().write(JSON.toJSONString(message));
                break;
        }
    }


    /**
     * 删除数据
     * @param response
     * @param data
     * @throws Exception
     */
    @RequestMapping(value = "/del", method = RequestMethod.POST)
    public void add(HttpServletResponse response, String data) throws Exception{
        response.setCharacterEncoding("UTF-8");
        response.setContentType("application/json; charset=utf-8");
        Message message = new Message();

        if (data == null) {
            message.setState(0);
            message.setMessage("数据为空");
            response.getWriter().write(JSON.toJSONString(message));
            return;
        }

        if (servace.del(data) == 1) {
            message.setState(1);
            message.setMessage("删除成功");
            response.getWriter().write(JSON.toJSONString(message));
        }
        else {
            message.setState(1);
            message.setMessage("未知错误");
            response.getWriter().write(JSON.toJSONString(message));
        }
    }


}
