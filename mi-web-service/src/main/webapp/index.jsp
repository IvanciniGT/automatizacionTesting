<%@ page language="java" contentType="text/json"
    pageEncoding="UTF-8"%>
<%
int a=Integer.parseInt(request.getParameter("numero1"));
int b=Integer.parseInt(request.getParameter("numero2"));
%>
{
    'resultado': <%= (a+b) %>
}