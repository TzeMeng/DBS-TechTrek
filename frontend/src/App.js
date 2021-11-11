import logo from './logo.svg';
import './App.css';
import { Link, BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Overview from './pages/Overview';
import Login from './pages/Login';
import Projects from './pages/Projects';
import Expense from './pages/Expense';
import CreateExpense from './pages/CreateExpense';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <Overview />
        </Route>
        <Route path="/login">
          <Login />
        </Route>
        <Route path="/projects">
          <Projects />
        </Route>
        <Route path="/expenses" exact>
          <Overview />
        </Route>
        <Route path="/expenses/:expenseId">
          <Expense />
        </Route>
        <Route path="/createExpense">
          <CreateExpense />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
