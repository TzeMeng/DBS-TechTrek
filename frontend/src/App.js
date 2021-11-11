import './App.css';
import { Link, BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Overview from './pages/Overview';
import Login from './pages/Login';
import Projects from './pages/Projects';
import Expense from './pages/Expense';
import CreateExpense from './pages/CreateExpense';

function App() {
  return (
    <div className="App-container">
      <Router>
        <Switch>
          <Route exact path="/">
            <Overview />
          </Route>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/projects" exact>
            <Projects />
          </Route>
          <Route path="/projects/:projectId" exact>
            <Overview />
          </Route>
          <Route path="/expenses/:expenseId">
            <Expense />
          </Route>
          <Route path="/projects/:projectId/create">
            <CreateExpense />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
