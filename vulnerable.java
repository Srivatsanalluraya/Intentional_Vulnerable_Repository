import java.sql.*;
import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class InsecureApp extends HttpServlet {

    // Hardcoded DB credentials
    private static final String DB_URL = "jdbc:mysql://localhost:3306/test";
    private static final String DB_USER = "root";
    private static final String DB_PASS = "password123";

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String user = request.getParameter("user");
        String cmd  = request.getParameter("cmd");

        try {
            // SQL Injection
            Connection con = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(
                "SELECT * FROM users WHERE username = '" + user + "'"
            );

            // Command Injection
            Runtime.getRuntime().exec(cmd);

            // XSS
            response.getWriter().println("Hello " + user);

            // Sensitive data exposure
            while (rs.next()) {
                response.getWriter().println(rs.getString("password"));
            }

        } catch (Exception e) {
            // Information leakage
            e.printStackTrace(response.getWriter());
        }
    }
}
