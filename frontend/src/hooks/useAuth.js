import { useEffect, useState } from "react";

const loggedInKey = "isLoggedIn";
const tokenKey = "accessToken";
const userIdKey = "userId";

const useAuth = () => {
	// Keep track of authenticated status
	const [isLoggedIn, setIsLoggedIn] = useState(localStorage.getItem(loggedInKey));
	const [userId, setUserId] = useState(localStorage.getItem(userIdKey));

	const setLogin = (accessToken, userId) => {
		localStorage.setItem(tokenKey, accessToken);
		localStorage.setItem(userIdKey, userId);
		localStorage.setItem(loggedInKey, "true");
		setIsLoggedIn(true);
		setUserId(userId);
	}

	return {
		isLoggedIn,
		setLogin,
		userId,
	}
}
export default useAuth