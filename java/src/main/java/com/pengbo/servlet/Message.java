package com.pengbo.servlet;

import com.pengbo.pojo.User;

public class Message {
    private Integer state;
    private String message;
    private User user;

    public Integer getState() {
        return state;
    }

    public void setState(Integer state) {
        this.state = state;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    @Override
    public String toString() {
        return "Message{" +
                "state=" + state +
                ", message='" + message + '\'' +
                ", user=" + user +
                '}';
    }
}
