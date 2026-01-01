import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const Home = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [user, setUser] = useState(null);

  useEffect(() => {
    checkLoginStatus();
  }, []);

  const checkLoginStatus = () => {
    const userData = localStorage.getItem('user');
    if (userData) {
      setUser(JSON.parse(userData));
      setIsLoggedIn(true);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('user');
    setIsLoggedIn(false);
    setUser(null);
  };

  return (
    <div className="home-container">
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
                <Link className="nav-link active" to="/">Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/dealers">Dealers</Link>
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
                  <button className="btn btn-outline-light btn-sm" onClick={handleLogout}>Logout</button>
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

      {/* Hero Section */}
      <section className="hero-section">
        <div className="container text-center">
          <h1 className="display-4 fw-bold mb-4">Find Your Perfect Car</h1>
          <p className="lead mb-4">
            Discover the best car dealerships across the United States.
            Read reviews, compare options, and make informed decisions.
          </p>
          <div className="hero-buttons">
            <Link to="/dealers" className="btn btn-primary btn-lg me-3">
              <i className="fas fa-search me-2"></i>Browse Dealers
            </Link>
            {!isLoggedIn && (
              <Link to="/register" className="btn btn-outline-light btn-lg">
                <i className="fas fa-user-plus me-2"></i>Join Now
              </Link>
            )}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="features-section py-5">
        <div className="container">
          <div className="row text-center">
            <div className="col-md-4 mb-4">
              <div className="feature-card">
                <i className="fas fa-store fa-3x text-primary mb-3"></i>
                <h4>Find Dealers</h4>
                <p>Locate authorized dealerships in your area with detailed information and contact details.</p>
                <Link to="/dealers" className="btn btn-outline-primary">Browse Dealers</Link>
              </div>
            </div>
            <div className="col-md-4 mb-4">
              <div className="feature-card">
                <i className="fas fa-star fa-3x text-primary mb-3"></i>
                <h4>Read Reviews</h4>
                <p>Make informed decisions with authentic customer reviews and ratings from fellow car buyers.</p>
                {isLoggedIn ? (
                  <Link to="/dealers" className="btn btn-outline-primary">View Reviews</Link>
                ) : (
                  <Link to="/login" className="btn btn-outline-primary">Login to Review</Link>
                )}
              </div>
            </div>
            <div className="col-md-4 mb-4">
              <div className="feature-card">
                <i className="fas fa-car fa-3x text-primary mb-3"></i>
                <h4>Car Inventory</h4>
                <p>Explore our comprehensive database of car makes and models available at our dealerships.</p>
                <Link to="/dealers" className="btn btn-outline-primary">View Inventory</Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="stats-section bg-primary text-white py-5">
        <div className="container text-center">
          <h2 className="mb-4">Trusted by Thousands</h2>
          <div className="row">
            <div className="col-md-3">
              <h3 className="display-4 fw-bold">50+</h3>
              <p>Dealership Locations</p>
            </div>
            <div className="col-md-3">
              <h3 className="display-4 fw-bold">100K+</h3>
              <p>Happy Customers</p>
            </div>
            <div className="col-md-3">
              <h3 className="display-4 fw-bold">25+</h3>
              <p>Years of Excellence</p>
            </div>
            <div className="col-md-3">
              <h3 className="display-4 fw-bold">500+</h3>
              <p>Expert Staff</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-dark text-white py-4">
        <div className="container text-center">
          <p>&copy; 2024 Cars Dealership. All rights reserved.</p>
          <p>Experience the difference with America's most trusted car retailer.</p>
        </div>
      </footer>
    </div>
  );
};

export default Home;
