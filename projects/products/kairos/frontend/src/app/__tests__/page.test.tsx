import { render, screen } from '@testing-library/react'
import Home from '../page'

// Mock the pricing card component's fetch calls if needed, but it's triggered on click.
// We just want to test rendering.

describe('Home Page', () => {
  it('renders the Pricing cards correctly', () => {
    render(<Home />)
    
    // Check if the pricing section title is there
    expect(screen.getByText('Simple, Transparent Pricing')).toBeInTheDocument()
    
    // Check if the individual pricing cards are rendered
    expect(screen.getByText('Solo')).toBeInTheDocument()
    expect(screen.getByText('Pro')).toBeInTheDocument()
    expect(screen.getByText('Studio')).toBeInTheDocument()
    expect(screen.getByText('Agency')).toBeInTheDocument()

    // Check if specific prices are rendered
    expect(screen.getByText('$49')).toBeInTheDocument()
    expect(screen.getByText('$149')).toBeInTheDocument()
    expect(screen.getByText('$399')).toBeInTheDocument()
    expect(screen.getByText('$999')).toBeInTheDocument()
  })

  it('renders the Hero Section correctly', () => {
    render(<Home />)
    const elements = screen.getAllByText(/The opportune moment/i)
    expect(elements.length).toBeGreaterThan(0)
  })
})
