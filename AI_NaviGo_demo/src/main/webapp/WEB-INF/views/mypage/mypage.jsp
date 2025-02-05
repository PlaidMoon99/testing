<%--
  Created by IntelliJ IDEA.
  User: human-15
  Date: 25. 2. 5.
  Time: 오전 10:19
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html  lang="ko">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>my page</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/layout/style.css"/>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/main/main.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"/>
    <style>
        .google-btn {
            background-color: white;
            border: 2px solid #ccc;
            color: black;
        }
        .google-btn:hover {
            border-color: #888;
        }
        .custom-divider {
            margin: 8px 0;
        }
        .sign-up-divider {
            margin: 24px 0;
        }
    </style>
</head>
<body>

<!-- 헤더 포함 -->
<header id="top-header">
    <jsp:include page="/WEB-INF/views/layout/nav.jsp" />
</header>

<div class="mypage-container">
    <h2>나의 정보</h2>
</div>

<!-- 푸터 포함 -->
<jsp:include page="/WEB-INF/views/layout/footer.jsp" />

<!-- Bootstrap JS (Popper.js 포함) -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>


</body>
</html>
