import { useEffect, useState } from "react";
import { useHistory } from "react-router";

const loggedInKey = "isLoggedIn";
const tokenKey = "accessToken";
const userIdKey = "userId";

const useAuth = () => {
	// Keep track of authenticated status
	const [isLoggedIn, setIsLoggedIn] = useState(localStorage.getItem(loggedInKey));
	const [userId, setUserId] = useState(localStorage.getItem(userIdKey));
	const history = useHistory();

	useEffect(() => {
		if (!isLoggedIn) {
			history.push("/login");
		}
	}, [isLoggedIn])

	const setLogin = (accessToken, userId) => {
		localStorage.setItem(tokenKey, accessToken);
		localStorage.setItem(userIdKey, userId);
		localStorage.setItem(loggedInKey, "true");
		setIsLoggedIn(true);
		setUserId(userId);
	}

	const setLogout = () => {
		localStorage.removeItem(tokenKey);
		localStorage.removeItem(userIdKey);
		localStorage.removeItem(loggedInKey);
		setIsLoggedIn(false);
		setUserId(undefined);
	}

	return {
		isLoggedIn,
		setLogin,
		userId,
		setLogout,
	}
}
export default useAuth