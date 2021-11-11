import { useState } from "react";
import { useParams } from "react-router";
import useAuth from "../hooks/useAuth";
import { baseUrl, categories } from "../lib/config";
import styles from "../styles/IndividualExpense.module.css";

const Expense = () => {
	const { userId } = useAuth();
	const { expenseId } = useParams();
	const [loading, setLoading] = useState(true);
	const [description, setDescription] = useState();
	const [amount, setAmount] = useState();
	const [category, setCategory] = useState();
	const [expenseData, setExpenseData] = useState();

	// TODO: Query by expense
	const fetchExpenseData = async () => {
		const res = await fetch(baseUrl + `/expense/${expenseId}`, {
			method: "GET",
		})
		const data = await res.json();
		setDescription(data.Description);
		setAmount(data.Amount);
		setCategory(categories[data.Category_id]);
		setExpenseData(data);
		setLoading(false);
	}
	fetchExpenseData();
	
	if (loading) {
		return ("Loading...");
	}
	return (
		<div className={styles.outerPage}>
			<div className={styles.expensesContainer}>
				<h1>{expenseData.Name}</h1>
				<label>Description</label>
				<input
					className={styles.input}
					type="text"
					value={description}
					onChange={(e) => setDescription(e.value)}
				/>
				<label>Category</label>
				<input
					className={styles.inputCategory}
					list="categories"
					value={category}
					onChange={(e) => setCategory(e.value)}
				/>
				<datalist id="categories">
					<option value="Production"></option>
					<option value="Operation" />
					<option value="Financial" />
					<option value="Vendor" />
					<option value="Manpower" />
					<option value="Software" />
					<option value="Hardware" />
				</datalist>
				<label>Amount</label>
				<input
					className={styles.inputNumber}
					type="number"
					value={amount}
					onChange={(e) => setAmount(e.value)}
				/>
				<div className={styles.buttonsContainer}>
					<input
						type="submit"
						className={styles.submitButton}
					/>
					<button
						className={styles.deleteButton}
					>Delete</button>
				</div>
			</div>
		</div>
	)
}
export default Expense