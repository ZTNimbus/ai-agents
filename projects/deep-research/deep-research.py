import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)

async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk

# Custom CSS for a more polished, research-focused interface
custom_css = """
/* Main container styling */
.gradio-container {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    max-width: 900px !important;
    margin: auto;
    background: #0f172a !important;
    padding: 1rem;
}

/* Dark background for the entire app */
body, #root {
    background: #0f172a !important;
}

/* Header styling */
.header-container {
    text-align: center;
    padding: 2rem 1rem 1rem 1rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

.header-container h1 {
    color: white;
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    line-height: 1.2;
}

.header-container p {
    color: rgba(255, 255, 255, 0.95);
    font-size: 1.1rem;
    margin-top: 0.5rem;
}

/* Input section styling */
.input-section {
    background: #1e293b;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    margin-bottom: 1.5rem;
    border: 1px solid #334155;
}

/* Label styling */
.input-section label {
    color: #e0e7ff !important;
    font-weight: 500 !important;
    font-size: 1rem;
}

/* Textbox styling */
.input-section textarea {
    background: #334155 !important;
    border: 2px solid #475569 !important;
    border-radius: 8px !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
    color: #f1f5f9 !important;
    width: 100% !important;
}

.input-section textarea::placeholder {
    color: #94a3b8 !important;
}

.input-section textarea:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
    background: #3f4f66 !important;
}

/* Button styling */
.run-button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.75rem 2rem !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    color: white !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 6px rgba(102, 126, 234, 0.3) !important;
    width: 100%;
}

.run-button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4) !important;
}

.run-button:active {
    transform: translateY(0) !important;
}

/* Report section styling */
.report-section {
    background: #1e293b;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    min-height: 400px;
    border: 1px solid #334155;
    overflow-x: auto;
}

.report-section label {
    color: #e0e7ff !important;
    font-weight: 500 !important;
    font-size: 1rem;
}

.report-section .markdown {
    line-height: 1.8;
    color: #e2e8f0 !important;
    background: transparent !important;
    word-wrap: break-word;
    overflow-wrap: break-word;
}

.report-section .prose {
    color: #e2e8f0 !important;
    max-width: 100% !important;
}

.report-section h1, .report-section h2, .report-section h3 {
    color: #a5b4fc !important;
    margin-top: 1.5rem;
    margin-bottom: 1rem;
    word-wrap: break-word;
}

.report-section p {
    color: #e2e8f0 !important;
    word-wrap: break-word;
}

.report-section em {
    color: #94a3b8 !important;
}

.report-section a {
    color: #818cf8 !important;
    text-decoration: none;
    border-bottom: 1px solid rgba(129, 140, 248, 0.3);
    transition: all 0.2s ease;
    word-break: break-all;
}

.report-section a:hover {
    border-bottom-color: #818cf8 !important;
    color: #a5b4fc !important;
}

/* Code blocks in report */
.report-section pre {
    overflow-x: auto;
    max-width: 100%;
}

.report-section code {
    word-wrap: break-word;
    white-space: pre-wrap;
}

/* Loading state */
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.6; }
}

.loading {
    animation: pulse 2s ease-in-out infinite;
}

/* Footer styling */
.footer {
    text-align: center;
    padding: 2rem 1rem;
    color: #94a3b8;
    font-size: 0.9rem;
}

/* Override any white backgrounds */
.gr-box, .gr-form, .gr-panel {
    background: transparent !important;
}

/* ============================================
   RESPONSIVE DESIGN - MOBILE FIRST
   ============================================ */

/* Tablets and smaller (landscape phones) */
@media (max-width: 768px) {
    .gradio-container {
        padding: 0.5rem;
        max-width: 100% !important;
    }
    
    .header-container {
        padding: 1.5rem 1rem;
        margin-bottom: 1.5rem;
        border-radius: 8px;
    }
    
    .header-container h1 {
        font-size: 2rem;
    }
    
    .header-container p {
        font-size: 1rem;
    }
    
    .input-section {
        padding: 1.25rem;
        border-radius: 8px;
        margin-bottom: 1.25rem;
    }
    
    .input-section label {
        font-size: 0.95rem;
    }
    
    .input-section textarea {
        font-size: 0.95rem !important;
    }
    
    .run-button {
        padding: 0.7rem 1.5rem !important;
        font-size: 0.95rem !important;
    }
    
    .report-section {
        padding: 1.5rem;
        min-height: 300px;
        border-radius: 8px;
    }
    
    .report-section label {
        font-size: 0.95rem;
    }
    
    .footer {
        padding: 1.5rem 1rem;
        font-size: 0.85rem;
    }
}

/* Mobile phones (portrait) */
@media (max-width: 480px) {
    .gradio-container {
        padding: 0.25rem;
    }
    
    .header-container {
        padding: 1.25rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 6px;
    }
    
    .header-container h1 {
        font-size: 1.75rem;
    }
    
    .header-container p {
        font-size: 0.9rem;
        margin-top: 0.25rem;
    }
    
    .input-section {
        padding: 1rem;
        border-radius: 6px;
        margin-bottom: 1rem;
    }
    
    .input-section label {
        font-size: 0.9rem;
    }
    
    .input-section textarea {
        font-size: 0.9rem !important;
        padding: 0.75rem !important;
    }
    
    .run-button {
        padding: 0.65rem 1.25rem !important;
        font-size: 0.9rem !important;
        border-radius: 6px !important;
    }
    
    .report-section {
        padding: 1rem;
        min-height: 250px;
        border-radius: 6px;
    }
    
    .report-section label {
        font-size: 0.9rem;
    }
    
    .report-section .markdown {
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    .report-section h1 {
        font-size: 1.5rem !important;
    }
    
    .report-section h2 {
        font-size: 1.3rem !important;
    }
    
    .report-section h3 {
        font-size: 1.1rem !important;
    }
    
    .footer {
        padding: 1rem 0.5rem;
        font-size: 0.8rem;
    }
}

/* Very small phones */
@media (max-width: 360px) {
    .header-container h1 {
        font-size: 1.5rem;
    }
    
    .header-container p {
        font-size: 0.85rem;
    }
    
    .input-section {
        padding: 0.75rem;
    }
    
    .run-button {
        padding: 0.6rem 1rem !important;
        font-size: 0.85rem !important;
    }
    
    .report-section {
        padding: 0.75rem;
    }
}

/* Desktop and laptop - FIXED WIDTH */
@media (min-width: 769px) {
    .gradio-container {
        max-width: 900px !important;
        width: 900px !important;
    }
}

/* Touch device optimizations */
@media (hover: none) and (pointer: coarse) {
    .run-button {
        padding: 0.85rem 2rem !important;
        min-height: 48px;
    }
    
    .input-section textarea {
        font-size: 16px !important; /* Prevents zoom on iOS */
    }
    
    /* Increase tap targets */
    .run-button:active {
        transform: scale(0.98) !important;
    }
}

/* Landscape mobile orientation */
@media (max-height: 500px) and (orientation: landscape) {
    .header-container {
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    .header-container h1 {
        font-size: 1.5rem;
    }
    
    .header-container p {
        font-size: 0.9rem;
    }
    
    .report-section {
        min-height: 200px;
    }
}

/* Print styles */
@media print {
    .header-container,
    .input-section,
    .run-button,
    .footer {
        display: none;
    }
    
    .report-section {
        box-shadow: none;
        border: 1px solid #ccc;
        background: white !important;
    }
    
    .report-section .markdown,
    .report-section p,
    .report-section h1,
    .report-section h2,
    .report-section h3 {
        color: black !important;
    }
}
"""

with gr.Blocks(theme=gr.themes.Soft(primary_hue="purple", secondary_hue="blue"), css=custom_css) as ui: # type: ignore
    # Header
    with gr.Column(elem_classes="header-container"):
        gr.Markdown(
            """
            # 🔬 Deep Research
            ### Comprehensive AI-powered research at your fingertips
            """
        )
    
    # Input Section
    with gr.Column(elem_classes="input-section"):
        query_textbox = gr.Textbox(
            label="What topic would you like to research?",
            placeholder="Enter your research question or topic here...",
            lines=3
        )
        
        run_button = gr.Button("🚀 Start Research", variant="primary", elem_classes="run-button")
    
    # Report Section
    with gr.Column(elem_classes="report-section"):
        report = gr.Markdown(
            label="Research Report",
            value="*Your research report will appear here...*"
        )
    
    # Footer
    with gr.Column(elem_classes="footer"):
        gr.Markdown("Powered by AI • Made by Kaya ATASOY")
    
    # Event handlers
    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)