# FinStart – FinTech Financial Super-App (College Project)

**FinStart** is a mobile-first financial super-app simulation designed for college students and young adults. It promotes financial literacy, budget discipline, and wealth-building awareness through an interactive, educational sandbox.

> ⚠️ **DEMO MODE — NO REAL MONEY**: FinStart is an educational simulator. All balances, bank accounts, and transactions are completely virtual and local. No real money or banking credentials are used or collected.

---

## 🚀 How to Run & Deploy the Application

### 1. Deploying to Streamlit Community Cloud (Recommended)
This repository is pre-configured for instant zero-configuration deployment to **[Streamlit Community Cloud](https://streamlit.io/cloud)**:
1. Push this project repository to your GitHub account.
2. In Streamlit Cloud, click **"New app"**.
3. Select your repository and branch (`main`).
4. Set **Main file path** to `streamlit_app.py` (or `app.py`).
5. Click **Deploy!**

The self-contained React frontend in `dist/index.html` is automatically served within Streamlit Components without needing Node.js in the cloud container.

---

### 2. Run Locally with Streamlit
```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Run the Streamlit super-app
streamlit run streamlit_app.py
```
Your browser will open automatically at **[http://localhost:8501](http://localhost:8501)**.

---

### 3. Run Locally with Vite (React Hot-Reload)
```bash
# 1. Install Node dependencies
npm install

# 2. Start Vite dev server
npm run dev

# 3. Or build production bundle
npm run build
```
Access the Vite dev server at **[http://localhost:5173](http://localhost:5173)**.

---

## 🛠️ Technology Stack

- **Frontend Core**: React 19 + TypeScript + Vite
- **Styling**: Tailwind CSS with custom Dark Forest Green financial palette (`#064e3b`, `#047857`, `#10b981`)
- **Visual Charts**: Recharts (Responsive bar charts, donut charts, area charts, and gauges)
- **Icons**: Lucide React icons
- **State & Storage**: React Context API + LocalStorage persistence layer
- **Celebrations**: Canvas Confetti for goal milestones & successful transactions
- **Backend Architecture**: Supabase-ready client abstraction (`src/services/supabaseClient.ts`)

---

## 📱 The Eight Core Sections

1. **Welcome & Onboarding**:
   - Persona selection: *College Student*, *Young Professional*, or *Campus Freelancer*.
   - Guided introduction to financial literacy concepts.
   - Initial financial parameters setup.

2. **Financial Profile**:
   - Editable monthly income / allowance base.
   - Monthly expenses split: Essential Needs vs Discretionary Wants.
   - The **50/30/20 Rule Analysis** check for student budgets.
   - Investment risk tolerance configuration (Conservative, Balanced, Aggressive).

3. **Main Dashboard**:
   - Real-time KPI metric cards: Total Virtual Wealth, Available Wallet Balance, Goals Progress, Health Score.
   - Interactive **Monthly Cash Flow Trend BarChart** (Inflow vs Outflow vs Savings surplus).
   - **Expense Category Donut PieChart** (Dining, Books, Transit, Outings, Shopping).
   - Quick Action hub (Pay/Transfer, Add Funds, Save, Calculate Loan).
   - Recent Transactions feed with instant receipt preview.

4. **Virtual Wallet & Simulated Payments**:
   - Starts with **₹10,000** in virtual funds.
   - **Deposit Funds**: Top-up wallet from simulated sources (Allowance, Hackathon Prize, Gigs).
   - **Send Money**: Pay fictional campus contacts (Campus Cafeteria, Bookstore Hub, Roommates) or custom UPI VPAs.
   - **Strict Validation**: Prevents overspending and negative balances with immediate user alerts.
   - **Verifiable Receipt Modal**: Generates a unique transaction reference (`TXN-YYYYMMDD-XXXX`), status badge, and print/copy capabilities.
   - Searchable, filterable transaction ledger with CSV export.

5. **Savings Goals**:
   - Preloaded student targets: Emergency Cushion, Coding Laptop Upgrade, Certifications, Semester Trip.
   - Direct transfer from virtual wallet to goals (and emergency returns back to wallet).
   - Visual progress bars, target dates, remaining amounts, and milestone confetti celebrations.

6. **Loan & EMI Simulator**:
   - Interactive sliders and number inputs for Principal (up to ₹30 Lakhs), Annual Interest (3% - 24%), and Tenure (3 - 84 months).
   - Instant presets: *Student Higher Education Loan (8.5%)*, *Laptop Gadget Loan (11.5%)*, *Campus Bike Loan (10.0%)*, *Personal Micro-Loan (14.0%)*.
   - Donut chart comparing Principal vs Total Interest charged.
   - Comprehensive **Month-by-Month Amortization Schedule Table**.
   - Educational advisory on avoiding predatory instant loan apps.

7. **Investment Simulator & Compounding Modeler**:
   - **SIP Calculator**: Monthly contributions, expected returns, and time horizon with multi-year AreaChart growth projections.
   - **Asset Allocation Matrix**: Conservative, Balanced, and Aggressive portfolio strategies.
   - **Virtual Investment Sandbox**: Allocate virtual wallet funds into demo assets (Nifty 50 Index Fund, Sovereign Gold Bonds, Liquid Savings, Clean Tech) and track demo performance.

8. **Financial Health Score & Personalized Insights**:
   - Transparent **100-point Financial Health Score Gauge**.
   - 4-Pillar scoring engine (25 pts each):
     1. Savings Ratio Discipline
     2. Emergency Cushion Runway (Months of living expenses buffered)
     3. Budget & Outflow Discipline (Keeping burn under 65%)
     4. Goal Commitment & Consistency
   - Dynamic, personalized recommendations linking to relevant tools.
   - **Reset Demo Data**: One-click restore button returning wallet to fresh ₹10,000 state.

---

## 🗄️ Architecture & Future Supabase Integration

FinStart is architected with a decoupled service layer. When ready to connect Supabase:
1. Set up `.env` with `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY`.
2. Install `@supabase/supabase-js`.
3. Execute the provided PostgreSQL schema included in `src/services/supabaseClient.ts`.
