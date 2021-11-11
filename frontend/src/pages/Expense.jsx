import { useState } from "react";
import useAuth from "../hooks/useAuth";
import { categories } from "../lib/config";
import styles from "../styles/IndividualExpense.module.css";

const Expense = () => {
	const { userId } = useAuth();

	// TODO: Query by expense
	
	// dummy data
	const expenseInfo = {
        id: 1,
        project_id: 2,
        category_id: 2,
        name: "Server Maintenance",
        description: "Server maintenance and upgrading work to incorporate BC plans",
        amount: 30000,
        created_at: "2021-11-04T16:00:00.000Z",
        created_by: "Jacky",
        updated_at: "2021-11-06T16:00:00.000Z",
        updated_by: "Jacky"
    }

	const [description, setDescription] = useState(expenseInfo.description);
	const [amount, setAmount] = useState(expenseInfo.amount);
	const [category, setCategory] = useState(categories[expenseInfo.category_id])

	return (
		<div className={styles.outerPage}>
			<div className={styles.expensesContainer}>
				<h1>{expenseInfo.name}</h1>
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