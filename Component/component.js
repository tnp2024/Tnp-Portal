/*class for sidebar*/
class Sidebar extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <nav class='sidebar close'>
        <header>
            <div class='image-text'>
                <span class='image'>
                </span>

                <div class='text logo-text'>
                    <span class='name'>Aarti Pentawar </span>
                    <span class='profession'>T&P Admin</span>
                </div>
            </div>

            <i class='bx bx-chevron-right toggle'></i>
        </header>

        <div class='menu-bar'>
            <div class='menu'>

                <li class='search-box'>
                    <i class='bx bx-search icon'></i>
                    <input type='text' placeholder='Search...'>
                </li>

                <ul class='menu-links'>
                    <li class='nav-link'>
                    <a href="Dashboard">
                    <i class='bx bx-home-alt icon' ></i>
                            <span class='text nav-text'>Dashboard</span>
                        </a>
                    </li>

                    <li class='nav-link'>
                        <a href='C:\UiKit\TNP ADMIN\Drive\Drive.html'>
                            <i class='bx bxs-collection icon' ></i>
                            <span class='text nav-text'>Drives</span>
                        </a>
                    </li>

                    <li class='nav-link'>
                        <a href='#'>
                            <i class='bx bxs-collection icon'></i>
                            <span class='text nav-text'>Activity</span>
                        </a>
                    </li>

                    <li class='nav-link'>
                        <a href='#'>
                            <i class='bx bxs-data icon' ></i>
                            <span class='text nav-text'>Student DB</span>
                        </a>
                    </li>

                    <li class='nav-link'>
                        <a href='#'>
                            <i class='bx bxs-data icon' ></i>
                            <span class='text nav-text'>Coordinator DB</span>
                        </a>
                    </li>

                </ul>
            </div>

            <div class='bottom-content'>

                <li class=''>
                    <a href='#'>
                        <i class='bx bxs-bell-ring icon' ></i>
                        <span class='text nav-text'>Notification</span>
                    </a>
                </li>

                <li class=''>
                    <a href='#'>
                        <i class='bx bx-link icon' ></i>
                        <span class='text nav-text'>ERP</span>
                    </a>
                </li>

                <li class=''>
                    <a href='#'>
                        <i class='bx bx-log-out icon' ></i>
                        <span class='text nav-text'>Logout</span>
                    </a>
                </li>

                <li class='mode'>
                    <div class='sun-moon'>
                        <i class='bx bx-moon icon moon'></i>
                        <i class='bx bx-sun icon sun'></i>
                    </div>

                    <span class='mode-text text'>Dark mode</span>

                    <div class='toggle-switch'>
                        <span class='switch'></span>
                    </div>
                </li>
                
            </div>
        </div>

    </nav>

    
    <script src="Sidebar.js"></script>
    
    `;
    }
}
customElements.define('app-sidebar', Sidebar);


/*class for create drive form*/

class CreateDrive extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <div class="card">
  <h1 class="dropdown-btn">Create Drive</h1>
  <div class="card-body hidden">
    <form id="jobForm" action="submit_form_url" method="POST">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" class="form-control" id="title" name="title" placeholder="Enter job title" required>
      </div>
      <div class="form-group">
        <label for="company_name">Company Name:</label>
        <input type="text" class="form-control" id="company_name" name="company_name" placeholder="Enter company name" required>
      </div>
      <div class="form-group">
        <label for="date">Date:</label>
        <input type="date" class="form-control" id="date" name="date" required>
      </div>
      <div class="form-group">
        <label for="content">Content:</label>
        <textarea class="form-control" id="content" name="content" placeholder="Enter job content" required></textarea>
      </div>
      <div class="form-group">
        <label for="Bond">Bond:</label>
        <input type="text" class="form-control" id="Bond" name="Bond" placeholder="Enter bond details" required>
      </div>
      <div class="form-group">
        <label for="industry_type">Industry Type:</label>
        <input type="text" class="form-control" id="industry_type" name="industry_type" placeholder="Enter industry type" required>
      </div>
      <div class="form-group">
        <label>Department:</label><br>
        <div class="checkbox-group">
            <input type="checkbox" id="civil_with_computer" name="department" value="Civil Engineering With Computer Applications">
            <label for="civil_with_computer">Civil Engineering With Computer Applications</label><br>

            <input type="checkbox" id="robotics_ai" name="department" value="Robotics and Artificial Intelligence">
            <label for="robotics_ai">Robotics and Artificial Intelligence</label><br>

            <input type="checkbox" id="mechanical_mechatronics" name="department" value="Mechanical and Mechatronics Engineering (Additive Manufacturing)">
            <label for="mechanical_mechatronics">Mechanical and Mechatronics Engineering (Additive Manufacturing)</label><br>

            <input type="checkbox" id="mechanical" name="department" value="Mechanical Engineering">
            <label for="mechanical">Mechanical Engineering</label><br>

            <input type="checkbox" id="electronics_computer" name="department" value="Electronics and Computer Engineering">
            <label for="electronics_computer">Electronics and Computer Engineering</label><br>

            <input type="checkbox" id="electrical_computer" name="department" value="Electrical and Computer Engineering">
            <label for="electrical_computer">Electrical and Computer Engineering</label><br>

            <input type="checkbox" id="computer_science" name="department" value="Computer Science and Engineering">
            <label for="computer_science">Computer Science and Engineering</label><br>

            <input type="checkbox" id="civil_construction" name="department" value="Civil Engineering (Construction Technology)">
            <label for="civil_construction">Civil Engineering (Construction Technology)</label><br>

            <input type="checkbox" id="civil" name="department" value="Civil Engineering">
            <label for="civil">Civil Engineering</label><br>

            <input type="checkbox" id="chemical" name="department" value="Chemical Engineering">
            <label for="chemical">Chemical Engineering</label><br>

            <input type="checkbox" id="ai_data_science" name="department" value="Artificial Intelligence and Data Science">
            <label for="ai_data_science">Artificial Intelligence and Data Science</label><br>

            <input type="checkbox" id="architecture" name="department" value="Architecture">
            <label for="architecture">Architecture</label><br>
        </div>
    </div>
      <div class="form-group">
        <label for="job_role">Job Role:</label>
        <input type="text" class="form-control" id="job_role" name="job_role" placeholder="Enter job role" required>
      </div>
      <div class="form-group">
        <label for="job_location">Job Location:</label>
        <input type="text" class="form-control" id="job_location" name="job_location" placeholder="Enter job location" required>
      </div>
      <div class="form-group">
        <label for="job_eligibility">Job Eligibility:</label>
        <textarea class="form-control" id="job_eligibility" name="job_eligibility" placeholder="Enter job eligibility" required></textarea>
      </div>
      <div class="form-group">
        <label for="selection_process">Selection Process:</label>
        <textarea class="form-control" id="selection_process" name="selection_process" placeholder="Enter selection process" required></textarea>
      </div>
      <div class="form-group">
        <label for="job_CTC">Job CTC:</label>
        <input type="text" class="form-control" id="job_CTC" name="job_CTC" placeholder="Enter job CTC" required>
      </div>
      
      <button type="submit" class="btn btn-submit">Create</button>
    </form>
  </div>
</div>

<script src="CreateDrive.js"></script>
        
        `;
    }
}
customElements.define('app-createdrive', CreateDrive);

/* class for single drive card*/

class Drive extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <div class="container">
            <div class="card">
            <div class="img">
               <img src="#">
            </div>
            <div class="top-text">
               <div class="name">
                  Accenture
               </div>
               <p>
                  CSE, IT, ECE
               </p>
            </div>
            <div class="bottom-text">
               <div class="text">
                  Job Role: Data Analyst
               </div>
            <div class="btn">
                  <a href="#">Read more</a>
            </div>
               
        </div>
    </div>
</div>
        
        `;
    }
}
customElements.define('app-drive', Drive);


/*class for activity*/
class Activity extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <div class="container">
            <div class="card">
            <div class="img">
               <img src="#">
            </div>
            <div class="top-text">
               <div class="name">
                  Accenture
               </div>
               <p>
                  CSE, IT, ECE
               </p>
            </div>
            <div class="bottom-text">
               <div class="text">
                  Job Role: Data Analyst
               </div>
            <div class="btn">
                  <a href="#">Read more</a>
            </div>
               
        </div>
    </div>
</div>
        
        `;
    }
}
customElements.define('app-activity', Activity);