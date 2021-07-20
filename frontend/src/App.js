import React from 'react';
import axios from 'axios';
import AuthorList from './components/Authors';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': [],
            'nav': [],
        };
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/')
            .then(
                response => {
                    const authors = response.data
                    this.setState({
                        'authors': authors
                    })
                }
            ).catch(
            error => console.log(error)
        )
    }

    render() {
        return (
            <div>
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                    <div className="container-fluid">
                        <a className="navbar-brand" href="#">Navbar</a>
                        <div className="collapse navbar-collapse" id="navbarNav">
                            <ul className="navbar-nav">
                                <li className="nav-item">
                                    <a className="nav-link active" aria-current="page" href="#">Home</a>
                                </li>
                                <li className="nav-item">
                                    <a className="nav-link" href="#">Features</a>
                                </li>
                                <li className="nav-item">
                                    <a className="nav-link" href="#">Pricing</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                <AuthorList authors={this.state.authors}/>
                <footer>
                    <h5>There some footer</h5>
                </footer>
            </div>

        )
    };
}

export default App;
