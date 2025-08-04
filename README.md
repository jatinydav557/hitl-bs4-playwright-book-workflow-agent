▶️ YouTube Demo: [Watch Here](https://www.youtube.com/watch?v=B3IQRdgbdDM&list=PLe-YIIlt-fbNajMvdZoBUdjZNbmLOMJSU&index=2&ab_channel=Jatin)  
# 📕Softnerve Book Agent - Automated Book Publication Workflow

An advanced automated chapter rewriter with multi-agent AI system, Human-in-the-Loop (HITL) capabilities, RL-based reward system, and semantic search using LangGraph.

## 🎯 Overview

This application provides a comprehensive automated book publication workflow that:

- **Scrapes & Captures**: Fetches content from web URLs with full-page screenshots
- **AI-Driven Writing**: Uses multiple AI agents (Writer, Reviewer, Editor) for content creation and refinement
- **Human-in-the-Loop**: Facilitates multiple iterations with human input for writers, reviewers, and editors
- **RL-Based Rewards**: Advanced reinforcement learning reward system with multiple quality metrics
- **Semantic Search**: Enhanced ChromaDB with semantic search and version tracking
- **Agentic API**: Seamless content flow between AI agents with comprehensive metadata

## 🚀 Quick Start

1. **Create environment and install dependencies:**

   ```bash
   uv venv --python=3.10
   uv pip install -r requirements.txt
   ```

2. **Install Playwright browsers (required for screenshots):**

   ```bash
   playwright install
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root with:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Get your free API key from [Groq Console](https://console.groq.com/)

4. **Run the application:**

   ```bash
   streamlit run main.py
   ```

5. **Open your browser** to the URL shown (usually http://localhost:8501)

## 🏗️ Architecture

### Multi-Agent Workflow

The application uses LangGraph to orchestrate a sophisticated workflow with the following agents:

1. **📖 Scraper**: Extracts text from web pages with robust error handling
2. **📸 Screenshot**: Captures visual snapshots of source pages
3. **✍️ AI Writer**: Creative content generation with multiple writing styles
4. **🔍 AI Reviewer**: Comprehensive content analysis and quality assessment
5. **✏️ AI Editor**: Final refinements and publication optimization
6. **👥 Human Review**: Interactive human-in-the-loop review process
7. **🎯 RL Reward Model**: Advanced quality scoring with multiple metrics
8. **💾 Vector Store**: Enhanced ChromaDB with semantic search

### AI Agent Capabilities

#### 🤖 AI Writer

- **Multiple Writing Styles**: Modern, classic, dramatic, conversational, academic
- **Dialogue Enhancement**: Natural speech patterns and character development
- **Descriptive Elements**: Rich sensory details and atmospheric descriptions

#### 🔍 AI Reviewer

- **Content Quality Analysis**: Preservation, improvement, engagement assessment
- **Grammar & Style Check**: Comprehensive writing mechanics review
- **Engagement & Flow**: Narrative pacing and reader engagement evaluation

#### ✏️ AI Editor

- **Feedback Application**: Incorporates review feedback into improvements
- **Final Polish**: Publication-ready refinements
- **Audience Optimization**: Tailored for specific target audiences
- **Metadata Generation**: Automatic title, summary, and keyword generation

### 🎯 RL-Based Reward System

Advanced reinforcement learning reward model with multiple quality metrics:

- **Readability Score**: Flesch Reading Ease calculation
- **Engagement Score**: Vocabulary diversity and sentence variety
- **Coherence Score**: Transition words and logical flow
- **Semantic Similarity**: Content preservation assessment
- **AI Quality Score**: LLM-based quality evaluation

### 🔍 Enhanced Vector Store

ChromaDB with advanced features:

- **Semantic Search**: Find similar content across all versions
- **Version History**: Track all iterations and improvements
- **Metadata Tracking**: Comprehensive version information
- **Quality Filtering**: Find best-performing versions
- **Statistics**: Overall system performance metrics

## 🎛️ Configuration Options

### Workflow Settings

- **AI Agents**: Enable/disable the multi-agent AI workflow
- **Human Review**: Enable/disable human-in-the-loop review
- **Writing Style**: Choose from modern, classic, dramatic, conversational, academic
- **Target Audience**: Optimize for general, academic, commercial, or literary audiences

### Search & Analytics

- **Semantic Search**: Search across all stored versions
- **Version History**: View all processed versions
- **Quality Metrics**: Track reward scores and improvements
- **Statistics**: System-wide performance analytics

## 📊 Features

### Core Capabilities

- **📖 Web Scraping**: Robust text extraction from URLs with error handling
- **🤖 Multi-Agent AI**: Writer, Reviewer, Editor agents with specialized capabilities
- **📸 Screenshot Capture**: Full-page visual snapshots of source pages
- **👥 Human Review**: Interactive editing and approval workflow
- **📊 Advanced Analytics**: Comprehensive quality metrics and scoring
- **🔍 Semantic Search**: Find similar content across all versions
- **💾 Version Control**: Complete history tracking with metadata

### Quality Assurance

- **RL-Based Rewards**: Multi-dimensional quality scoring
- **AI Assessment**: LLM-powered content evaluation
- **Human Oversight**: Interactive review and editing
- **Iterative Improvement**: Multiple refinement cycles
- **Publication Ready**: Optimized for specific audiences

### Data Management

- **Vector Storage**: ChromaDB with semantic search
- **Metadata Tracking**: Comprehensive version information
- **Search Capabilities**: Find content by similarity or quality
- **Statistics**: System performance and quality metrics
- **Export Options**: Version history and analytics

## 🔧 Troubleshooting

### Common Issues

- **"No rewritten text"**: Check your GROQ_API_KEY and internet connection
- **"Playwright not found"**: Run `playwright install` to install browsers
- **"ChromaDB error"**: Ensure ChromaDB is properly installed and accessible
- **"AI agents not working"**: Verify API key and model availability

### Performance Tips

- **Use AI Agents**: Enable for best quality results
- **Human Review**: Enable for critical content requiring human oversight
- **Writing Style**: Choose appropriate style for your content type
- **Target Audience**: Select audience for optimal publication optimization

## 📈 Advanced Usage

### Custom Workflows

The system supports custom workflow configurations:

- Basic workflow (scraper → rewriter → review → store)
- AI-enhanced workflow (scraper → AI agents → review → store)
- Automated workflow (scraper → AI agents → store)

### Quality Optimization

- Monitor reward scores to identify best-performing configurations
- Use semantic search to find similar high-quality content
- Review AI agent feedback for improvement insights
- Track version history for iterative improvements

### Publication Preparation

- Generate publication metadata automatically
- Optimize content for specific audiences
- Create engaging titles and summaries
- Track keywords and categorization

## 🤝 Contributing

This project demonstrates advanced AI agent orchestration, RL-based quality assessment, and human-in-the-loop workflows for automated book publication.
