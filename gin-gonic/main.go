package main

import (
	"net/http"
	"github.com/gin-gonic/gin"
)

type getapi struct {
    ID int `json:"id"`
    Name string `json:"name"`
}


func setupRouter() *gin.Engine {
	r := gin.Default()
	r.LoadHTMLGlob("web/templates/**/*")

	r.GET("/", func(c *gin.Context) {
        c.HTML(http.StatusOK, "index.go.tmpl", gin.H{
            "title": "Main website",
        })
    })

	var getapisarr = []getapi{
		{ID: 0, Name: "Thamognya Kodi"},
		{ID: 1, Name: "IDK"},
	}
	r.GET("/api/get", func(c *gin.Context) {
		c.IndentedJSON(http.StatusOK, getapisarr)
    })


    r.NoRoute(func(c *gin.Context) {
    	c.HTML(http.StatusNotFound, "404.go.tmpl", gin.H{
    		"title": "Not found",
    	})
	})

	return r
}

func main() {
    // gin.SetMode(gin.ReleaseMode)
	r := setupRouter()
	r.Run(":8080")
}
