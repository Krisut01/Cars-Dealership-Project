import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './Dealers.css';

const Dealers = () => {
  const [dealers, setDealers] = useState([]);
  const [filteredDealers, setFilteredDealers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedState, setSelectedState] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchDealers();
    checkLoginStatus();
  }, []);

  useEffect(() => {
    if (selectedState) {
      fetchDealersByState(selectedState);
    } else {
      setFilteredDealers(dealers);
    }
  }, [selectedState, dealers]);

  const fetchDealers = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/dealers/');
      setDealers(response.data);
      setFilteredDealers(response.data);
    } catch (error) {
      console.error('Error fetching dealers:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchDealersByState = async (state) => {
    try {
      const response = await axios.get(`http://localhost:8000/api/dealers/state/${state}/`);
      setFilteredDealers(response.data);
    } catch (error) {
      console.error('Error fetching dealers by state:', error);
    }
  };

  const checkLoginStatus = () => {
    const userData = localStorage.getItem('user');
    if (userData) {
      setUser(JSON.parse(userData));
      setIsLoggedIn(true);
    }
  };

  const handleStateChange = (e) => {
    setSelectedState(e.target.value);
  };

  const getUniqueStates = () => {
    const states = dealers.map(dealer => dealer.state);
    return [...new Set(states)].sort();
  };

  if (loading) {
    return <div className="loading">Loading dealers...</div>;
  }

  return (
    <div className="dealers-container">
      {/* Navigation */}
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container">
          <Link className="navbar-brand" to="/">
            <i className="fas fa-car"></i> Cars Dealership
          </Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <Link className="nav-link" to="/">Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link active" to="/dealers">Dealers</Link>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="http://localhost:8000/static/About.html">About Us</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="http://localhost:8000/static/Contact.html">Contact Us</a>
              </li>
              {isLoggedIn ? (
                <li className="nav-item">
                  <span className="navbar-text me-3">Welcome, {user?.first_name}!</span>
                  <button className="btn btn-outline-light btn-sm" onClick={() => {
                    localStorage.removeItem('user');
                    setIsLoggedIn(false);
                    setUser(null);
                  }}>Logout</button>
                </li>
              ) : (
                <li className="nav-item">
                  <Link className="btn btn-outline-light btn-sm me-2" to="/login">Login</Link>
                  <Link className="btn btn-primary btn-sm" to="/register">Register</Link>
                </li>
              )}
            </ul>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <div className="container mt-4">
        <div className="row">
          <div className="col-12">
            <h1 className="mb-4">Car Dealerships</h1>

            {/* Filter by State */}
            <div className="mb-4">
              <label htmlFor="stateFilter" className="form-label">Filter by State:</label>
              <select
                id="stateFilter"
                className="form-select w-auto"
                value={selectedState}
                onChange={handleStateChange}
              >
                <option value="">All States</option>
                {getUniqueStates().map(state => (
                  <option key={state} value={state}>{state}</option>
                ))}
              </select>
            </div>

            {/* Dealers Grid */}
            <div className="row">
              {filteredDealers.map(dealer => (
                <div key={dealer.id} className="col-md-6 col-lg-4 mb-4">
                  <div className="card h-100">
                    <div className="card-body">
                      <h5 className="card-title">{dealer.name}</h5>
                      <p className="card-text">
                        <i className="fas fa-map-marker-alt me-2"></i>
                        {dealer.address}<br />
                        {dealer.city}, {dealer.state} {dealer.zip_code}
                      </p>
                      <p className="card-text">
                        <i className="fas fa-phone me-2"></i>
                        {dealer.phone}
                      </p>
                      {dealer.website && (
                        <p className="card-text">
                          <i className="fas fa-globe me-2"></i>
                          <a href={dealer.website} target="_blank" rel="noopener noreferrer">
                            Visit Website
                          </a>
                        </p>
                      )}
                    </div>
                    <div className="card-footer">
                      <Link
                        to={`/dealer/${dealer.id}`}
                        className="btn btn-primary me-2"
                      >
                        View Details
                      </Link>
                      {isLoggedIn && (
                        <Link
                          to={`/dealer/${dealer.id}/review`}
                          className="btn btn-success"
                        >
                          Review Dealer
                        </Link>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {filteredDealers.length === 0 && (
              <div className="text-center mt-5">
                <p className="text-muted">No dealers found for the selected state.</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dealers;
