package main

import (
	"Server/controllers"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
    r := gin.Default()

    r.GET("/", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{"message": "Hello, World!"})
    })

	// register routes
	// inventory
	r.GET("/inventory", controllers.GetInventoryItems)
	r.GET("/inventory/:id", controllers.GetInventoryItem)
	r.POST("/inventory", controllers.AddInventoryItem)
	r.PATCH("/inventory/:id", controllers.EditInventoryItem)
	r.DELETE("/inventory/:id", controllers.DeleteInventoryItem)	

	// listings
	r.GET("/inventory", controllers.GetListings)
	r.GET("/inventory/:id", controllers.GetListing)
	r.POST("/inventory", controllers.AddListing)
	r.PATCH("/inventory/:id", controllers.EditListing)
	r.DELETE("/inventory/:id", controllers.DeleteListing)	

    r.Run() // defaults to 0.0.0.0:8080
}